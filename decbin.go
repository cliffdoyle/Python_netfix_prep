package main

import "fmt"


func decimalToBinary(n int)string{
	res:=""
	for n>0{
		dig:=n%2
		res=string(dig)+res
		n /=2

	}
return res
}

func main(){
	bin:=decimalToBinary(1)
	fmt.Println(bin)
}