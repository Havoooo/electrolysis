import core.generated

noncomputable theory

open bool
open [class] classical
open [notation] function
open [class] int
open [notation] list
open [class] nat
open [notation] prod.ops
open [notation] unit

definition test.main : sem (unit) :=
let' t1 ← (0 : int);
let' t2 ← (0 : int);
let' ret ← ⋆;
return (⋆)


