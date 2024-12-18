package main

import (
	"errors"
	"fmt"
)

type Stack []int

// define methods to manipulate stack
func (s *Stack) push(value int) {
	*s = append(*s, value)
}

//Pop removes and returns the top element of the stack
func(s *Stack)pop()(int,error){
if len(*s)==0{
	return 0, errors.New("stack is empty")
}
//get last element (Top of stack)
top:=(*s)[len(*s)-1]
//remove last element
*s=(*s)[:len(*s)-1]
return top,nil

}

func(s *Stack)Swap()error{
//check if the stack has at least two elements
	if len(*s)<2{
		return errors.New("Stack has fewer than 2 elements")

	}
	// topElement:=(*s)[len(*s)-1]
	// secondTopElement:=(*s)[len(*s)-2]
//Swap the two elements using the Go's multiple assignment
(*s)[len(*s)-1], (*s)[len(*s)-2] = (*s)[len(*s)-2], (*s)[len(*s)-1]
	return nil
}

//Function Rotate ra && rb shifts all elements of the stack up by 1 position
//Takes the first element of the stack and moves it to the end of the stack
//a=[1,2,3,4] becomes a=[2,3,4,1]
func (s *Stack)Rotate(){
	if len(*s)>1{
		firstElement:=(*s)[0] //Get first element
		*s=append((*s)[1:], firstElement) //Move the first element to the end
	}
}

//The reverse rotate operation shifts all elements of the stack down by 1
//position. It takes the last element of the stack and moves it to the top
//a=[1,2,3,4] becomes a=[4,1,2,3]
//...unpacks the slice to pass each individual element from (*s)[:len(*s)-1]
//to append function.
func(s *Stack)ReverseRotate(){
	if len(*s)>1{
		last:=(*s)[len(*s)-1]
		*s=append([]int{last}, (*s)[:len(*s)-1]...)
	}
}

//STEP 2:Define Push-Swap Instructions
//Now we define the set of instructions (pa,pb, e.t.c) using functions. These instructions
//manipulate the two stacks(a and b)

//pa: Push the top element of stack b to stack a
func pa(a,b *Stack){
	if len(*b)>0{
		value,_:=b.pop()
		a.push(value)
	}
}

//pb: Push the top element of stack a to stack b
func pb(a,b *Stack){
	if len(*a)>0{
		value,_:=a.pop()
		b.push(value)
	}
}

//sa: Swap the top two elements of stack a
func sa(a *Stack){
	_=a.Swap()
}

//sb:Swap the top two elements of stack b
func sb(b *Stack){
	_=b.Swap()
}

//ss: Swap the top two elements of both stacks a and b
func ss(a,b *Stack){
	sa(a)
	sb(b)
}

//ra: Rotate stack a
func ra(a *Stack){
	a.Rotate()
}

// rb: Rotate stack b
func rb(b *Stack) {
	b.Rotate()
}

// rr: Rotate both stacks a and b
func rr(a, b *Stack) {
	ra(a)
	rb(b)
}

// rra: Reverse rotate stack a
func rra(a *Stack) {
	a.ReverseRotate()
}

// rrb: Reverse rotate stack b
func rrb(b *Stack) {
	b.ReverseRotate()
}

// rrr: Reverse rotate both stacks a and b
func rrr(a, b *Stack) {
	rra(a)
	rrb(b)
}

//isSorted checks if a stack is sorted in ascending order
func isSorted(s Stack)bool{
	for i:=0;i<len(s)-1;i++{
		if s[i]>s[i+1]{
			return false
		}
	}
	return true
}

//PushSwap implements the push-swap algorithm
func PushSwap(a Stack)[]string{
	var b Stack
	var instructions []string

	for !isSorted(a) {
		if len(a)>1 && a[len(a)-1]>a[len(a)-2]{
			sa(&a)
			instructions = append(instructions, "sa")
		}else{
			pb(&a,&b)
			instructions = append(instructions, "pb")
		}
	}

	for len(b)>0{
		pa(&a,&b)
		instructions = append(instructions, "pa")
	}
	return instructions
}
// executeInstruction executes a single instruction on the stacks
func executeInstruction(instruction string, a, b *Stack) error {
	switch instruction {
	case "sa":
		sa(a)
	case "sb":
		sb(b)
	case "ss":
		ss(a, b)
	case "pa":
		pa(a, b)
	case "pb":
		pb(a, b)
	case "ra":
		ra(a)
	case "rb":
		rb(b)
	case "rr":
		rr(a, b)
	case "rra":
		rra(a)
	case "rrb":
		rrb(b)
	case "rrr":
		rrr(a, b)
	default:
		return errors.New("invalid instruction")
	}
	return nil
}

// checker verifies if the stack is sorted after executing instructions
func checker(a Stack, instructions []string) string {
	var b Stack
	for _, instruction := range instructions {
		err := executeInstruction(instruction, &a, &b)
		if err != nil {
			return "Error"
		}
	}

	if isSorted(a) && len(b) == 0 {
		return "OK"
	}
	return "KO"
}

func main() {
	s := &Stack{}
	s.push(56)
	// fmt.Println(s)
	s.push(87)
	s.push(78)
	// s.Swap()
	// s.Rotate()
	fmt.Println(s)

}