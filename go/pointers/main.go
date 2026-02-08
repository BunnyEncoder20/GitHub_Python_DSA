package main

import (
	"fmt"
)

func main() {
	fmt.Println("Variables in Go have 3 parts (more like values):")
	fmt.Println("name | type | value")
	fmt.Println("But, it also has an address. Think of it like a box in a warehouse. The value is inside the box and the box has a label of it's name and type. And it is stored a some address in the warehouse.")
	fmt.Println("So that when we need to go and get that box, we use the address.")
	fmt.Println("")
	fmt.Println("This address is the value which the ptr holds, when it is pointing to a variable")
	fmt.Println("Check the following example:")
	i, j := 42, 2701
	fmt.Print("Values of i and j: ")
	fmt.Println(i, j)
	fmt.Print("Address of i and j: ")
	fmt.Println(&i, &j)
	fmt.Print("Pointer of i and j: ")
	pi, pj := &i, &j
	fmt.Println(pi, pj)
	fmt.Println("")
	fmt.Println("& can be read as 'address of' while reading it in code.")
	fmt.Println("It is tricky to understand the * as it is used in 2 ways:")
	fmt.Println("1. When in before a type, eg: *int - it is consider any pointer type, read as an pointer pointing to an int, or pointer with vase int")
	fmt.Println("2. When it is before a variable, it is considered dereferencing: when we are getting the value at that pointer address.")
	fmt.Println("Consider the following exampls:")
	fmt.Print("Dereferencing the i and j pointers: ")
	fmt.Println(*pi, *pj)
	fmt.Print("Type of the pointers:")
	fmt.Printf("%T\n", pi)
	fmt.Println("Changing the value of *p:")
	*pi, *pj = *pi+100, *pj/37
	fmt.Println(*pi, *pj)

	fmt.Println("Pointers shine when we use them with functions. Though there is a trade off:")
	fmt.Println("1. When we use simple pass as value, the stack (memory) frame for that function gets a copy of the value. This is good for immutability, but also means that any changes that are made within this stack frame would not be reflected outside, i.e: the function which called it.")
	fmt.Println("2. When we use pass by reference using pointers, it is more memory efficient and the value gets directly changed, but we lose immutability and it can lead to bugs if we are not careful.")
	fmt.Println("\nConsider the following example:")
	num := 10
	ans := mySquare(num)
	fmt.Printf("nums: %d | ans: %d\n", num, ans)
	fmt.Println("As you can see, the original num is not changed, cause the changes within the func (which makes a new stack frame) do not leave that frame")
	ans = mySquareAddr(&num)
	fmt.Printf("nums: %d | ans: %d\n", num, ans)
	fmt.Println("Now the original value has also changed cause we passed a reference to the address of the original num. We don't even need a return in this function.")
}

func mySquare(num int) int {
	num *= num
	fmt.Printf("num: %d | num addr: %d\n", num, &num)
	return num
}

func mySquareAddr(p *int) int {
	*p *= *p
	fmt.Printf("num: %d | num addr: %d\n", *p, p)
	return *p
}
