package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func longestWord(s string) (string, int) {
	wd, ln := "", 0
	for _, word := range strings.Split(s, " ") {
		if len(word) > ln {
			wd, ln = word, len(word)
		}
	}
	return wd, ln
}

func main() {
	fname := os.Args[1]
	dat, err := ioutil.ReadFile(fname)
	if err != nil {
		panic(err)
	}
	replacer := strings.NewReplacer(".", " ", "\n", " ", "-", " ", "_", " ", "'", " ", "/", " ", ":", " ", "(", " ", ")", " ")
	t := string(dat)
	t = replacer.Replace(t)
	txt, ln := longestWord(t)
	fmt.Printf("%s\t%d", txt, ln)
}
