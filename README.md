# TAD
 TAD is an [esolang](https://en.wikipedia.org/wiki/Esoteric_programming_language) designed to explore the power of the integer data structure. Most languages meet the infinite storage requirement of Turing-completeness by using tapes or stacks that hold arbitrary numbers of small values. TAD attempts to satisfy this by instead allowing for a small number of unbounded non-negative integers.
 
 This page contains the current specification for TAD, an example interpreter in Python 3, and several example programs.
 
 It is currently unknown if TAD is Turing-complete, however it seems very likely that it can implement an [I/D Machine](https://esolangs.org/wiki/I/D_machine) or [Biwise Cyclic Tag](https://esolangs.org/wiki/Bitwise_Cyclic_Tag).

## Specification

The program acts on a single non-negative integer of unbounded size known as the `Number`. It is procedural, and interprets the program as a series of commands and loops. Any unrecognized characters are removed, as is text between paired `!`s, which serve as comments. Variables can be named any non-empty alphanumeric string. `Number` is initialized to zero. All variables are initialized when first assigned. They cannot be used until they have been assigned.
Command | Description
------- | -----------
`+` | Increments `Number`.
`-` | Decrements `Number`. Behaviour when decrementing 0 is undefined.
`#var` | Assigns the current state of `Number` to the variable `var`.
`=var` | Sets `Number` equal to variable `var`.
`#var[ ]` | Executes the code between matching brackets `var` times. If `var` is changed during the execution of the loop it does *not* impact the loop. If `var` is 0 it will not run the code at all.
`=var[ ]` | Executes the code between matching brackets until `Number` and variable `var` are equal. If `var` is changed during execution it does impact the loop. If `Value` is already equal to `var` it will not run the code at all.
`=>` | Reads input from the user and store it in the `Number`. | `=>`
`#<` | Outputs the `Number` to stdio. | `#<`

 TAD can handle an arbitrary but finite number of variables.
 
 
## Example
From [modulo.tad](https://github.com/thedashdude/TAD/blob/master/examples/modulo.tad):
```
!modulo!
!computes a mod b!
#0
#acc
#IF
+
#1
=>
#a
!take input for the second argument!
=>
#b
#a[
  =1
  #IF
  =acc
  +
  #acc

  =b[
    =0
    #IF
    =b
  ]
  #IF[
    =0
    #acc
  ]
]
=acc
#<
```

### Explanation
The lines `#0 #acc #IF + #1` create four new variables, named `0`, `acc`, `IF`, and `1`. The numeric literals are set to their equivalent values, but strictly speaking they are variables and could be assigned different values. At the end of this section `Number` holds a value of `1`, having been incremented to set the variable `1` to the correct value.

The next sequence of commands is `=> #a => #b`, which reads from the user twice, and assignes the values to the variables `a` and `b`. After this, the `Number` is the same as `b`, the last value read from the user.

We next start a loop to run `a` times (`#a[`).  In this loop, we  run the commands `=1 #IF =acc + #acc`. This sets the `Number` to 1, sets `IF` to 1, sets the `Number` to `acc`, then adds 1 to it and assigns that new value back to `acc`. Simply put, at the start of each loop we set `IF` to 1 and increment `acc`.

Next up we have two loops that don't actually loop. `=b[ =0 #IF =b ]` runs until `Number` is equal to `b`, which happens at the end of the loop. Effectively this is an if statement running if `Number != b`. If so, set `IF` to 0. `#IF[ =0 #acc ]`. The next loop runs `IF` times, which is either 0 or 1. If it does run, which is when `Number` *is* equal to `b`, the accumulator `acc` is reset to zero.

The last few commands close off the loop (`]`), and print out the accumulator `acc` (`=acc #<`). We have incremented from zero `a` times, wrapping back to 0 at `b`. This calculates `a` modulo `b`.



