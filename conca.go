package main 

import "fmt"

func ConcatAlternate(sli1,sli2 []int)[]int{
	res:=[]int{}

	first,sec:=sli1,sli2

	if len(sli2)>len(sli1){
		first,sec=sli2,sli1

	}

	for i:=0;i<len(first);i++{
		res = append(res,first[i] )
		if i<len(sec){
			res = append(res, sec[i])
		}
	}
	return res

}

func main() {
	fmt.Println(ConcatAlternate([]int{1, 2, 3}, []int{4, 5, 6}))
	 fmt.Println(ConcatAlternate([]int{2, 4, 6, 8, 10}, []int{1, 3, 5, 7, 9, 11}))
	 fmt.Println(ConcatAlternate([]int{1, 2, 3}, []int{4, 5, 6, 7, 8, 9}))
	 fmt.Println(ConcatAlternate([]int{1, 2, 3}, []int{}))
	//  fmt.Println(Test("hie"))
 }