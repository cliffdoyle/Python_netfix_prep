package main

import "fmt"

func Rot13(word string, num int) string{
	res := []rune{}
	for _,ch:= range word{
		if ch >='a'||ch<='z'{
			res = append(res, 'a'+(ch-'a'+rune(num)%26))
		}else if ch >='A'||ch<='Z'{
			res = append(res, 'A'+(ch-'A'+rune(num)%26))
		}else{
			res = append(res,ch)
		}

	}

	return string(res)
}

func main(){
	fmt.Println(Rot13("Hello",3))
}