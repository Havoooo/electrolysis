from doit import create_after
from pathlib import Path

ref = Path('ref')

def task_cargo_build():
    return {
        'actions': ['cargo build'],
        'targets': ['target/debug/electrolysis'],
    }

def task_electrolysis_thys():
    for crate in ['core', 'alloc', 'collections', 'fixedbitset']:
        p = Path('thys') / crate
        yield {
            'name': str(crate),
            'actions': [['cargo', 'run', crate]],
            'file_dep': [p / 'config.toml', 'target/debug/electrolysis'],
            'targets': [p / 'generated.lean'],
        }

def task_linja_thys():
    # relies on ninja dependency management
    return {
        'task_dep': ['electrolysis_thys'],
        'actions': ['(cd thys; linja)'],
    }

def task_electrolysis_ref():
    for p in list(ref.rglob('lib.rs')):
        yield {
            'name': str(p),
            'actions': [['cargo', 'run', p],
                        'rustc --crate-type lib -Z unstable-options --unpretty mir "{}" > "{}"'.format(p, p.with_name('mir'))] +
            ([['mv', p.with_name('generated.lean'), p.with_name('broken.lean')]]
             if '!' in str(p) else []),
            'file_dep': [p, 'target/debug/electrolysis'],
            'task_dep': ['electrolysis_thys'],
            #'targets': [p.with_name('generated.lean')],
        }

@create_after(executed='electrolysis_ref', target_regex=r'ref/index\.html')
def task_ref():
    return {
        'actions': ['(cd ref; ./make_ref.py)'],
        'file_dep': ['ref/make_ref.py'] + [p for p in list(ref.rglob('*')) if p.suffix in ['.rs', '.lean', '.md']],
        'targets': ['ref/index.html'],
    }

def task_linja_ref():
    return {
        'task_dep': ['linja_thys', 'electrolysis_ref'],
        'actions': ['(cd ref; linja)'],
    }
