package main

import "core:fmt"

main :: proc() {
  fmt.println("Hello World")
  div, mod := divmod_again(17,5)
  fmt.println("div:", div)
  fmt.println("mod:", mod)
}

divmod_again :: proc(a, b: int) -> (x,y: int) {
  return a / b, a % b
}
