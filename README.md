<p align="center">
  <img src="logo.png?raw=true"/>
</p>

# electrolysis

[![Gitter](https://badges.gitter.im/Kha/electrolysis.svg)](https://gitter.im/Kha/electrolysis?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## About

A tool for formally verifying Rust programs by transpiling them into definitions in the [Lean](http://leanprover.github.io/) theorem prover. 

* **Masters thesis: Simple Verification of Rust Programs via Functional Purification - [thesis](https://github.com/Kha/masters-thesis/raw/master/main.pdf)|[presentation](http://kha.github.io/electrolysis/presentation.pdf)**
* [Official reference and coverage](http://kha.github.io/electrolysis/)
* [Blog post: A Formal Verification of Rust's Binary Search Implementation](https://kha.github.io/2016/07/22/formally-verifying-rusts-binary-search.html)

## Installation

Because electrolysis uses `rustc`'s unstable private API, you need a nightly compiler. Because the API is _highly_ unstable, you need a very specific nightly version, for which you should use [rustup.rs](https://www.rustup.rs/). After installing `rustup`, you can build this project by executing
```
electrolysis$ rustup override add $(cat rust-nightly-version)
electrolysis$ rustup component add rust-src
electrolysis$ cargo run core
```
This will build the project and export all code from the `core` crate necessary for `binary_search` (see also [thys/core/config.toml](thys/core/config.toml)) into [thys/core/generated.lean](thys/core/generated.lean) (this file already exists in case you just want to examine the correctness proof).
