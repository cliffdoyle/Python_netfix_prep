package main

import (
	"fmt"
	"strings"
	// "unique"
)

func main() {
	emptymap := make(map[string]int)
	text := `this is sample text with several words '
'this is more sample text with some different words`

	texto:=strings.Fields(text)

	for _,word:=range texto{
		emptymap[word]++
	}

	unique:=make([]string,0,len(emptymap))

	for word := range emptymap{
		unique = append(unique, word)
	}
	fmt.Println(emptymap)
	fmt.Println("Total num of unique words", len(emptymap))

	fmt.Println(unique)
}