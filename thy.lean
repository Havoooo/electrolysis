import .generated

open int
open test

example (foo : Foo) : sem.terminates_with (λ r, r = 1) (Shape.area foo) := rfl
example (foo : Foo) : sem.terminates_with (λ r, r = -1) (Circle.radius foo) := rfl
