# TAD
 TAD is an [esolang](https://en.wikipedia.org/wiki/Esoteric_programming_language) designed to explore the power of the integer data structure. Most languages meet the infinite storage requirement of Turing-completeness by using tapes or stacks that hold arbitrary numbers of small values. TAD attempts to satisfy this by instead allowing for a small number of unbounded non-negative integers.
 
 This page contains the current specification for TAD, an example interpreter in Python 3, and several example programs.

## Specification

The program acts on a single non-negative integer of unbounded size known as the `Number`. It is procedural, and interprets the program as a series of commands and loops. Any unrecognized characters are removed, as is text between paired `!`s, which serve as comments. Variables can be named any non-empty alphanumeric string. 

Command | Description
------- | -----------
`+` | Increments `Number`.
`-` | Decrements `Number`. Behaviour when decrementing `0` is undefined.
`#var` | Assigns the current state of `Number` to the variable `var`.
`=var` | Sets `Number` equal to variable `var`.
`#var[ ]` | Executes the code between matching brackets `var` times. If `var` is changed during the execution of the loop it does *not* impact the loop. If `var` is `0` it will not run the code at all.
`=var[ ]` | Executes the code between matching brackets until `Number` and variable `var` are equal. If `var` is changed during execution it does impact the loop. If `Value` is already equal to `var` it will not run the code at all.
`=>` | Reads input from the user and store it in the `Number`. | `=>`
`#<` | Outputs the `Number` to stdio. | `#<`

 TAD can handle an arbitrary but finite number of variables.
 
