package main

import "fmt"

// Define the stack operations with logging
func sa(a []int) {
    if len(a) > 1 {
        a[0], a[1] = a[1], a[0]
        fmt.Println("sa")
    }
}

func ra(a []int) {
    if len(a) > 1 {
        first := a[0]
        copy(a, a[1:])
        a[len(a)-1] = first
        fmt.Println("ra")
    }
}

func rra(a []int) {
    if len(a) > 1 {
        last := a[len(a)-1]
        copy(a[1:], a)
        a[0] = last
        fmt.Println("rra")
    }
}

func pb(a, b *[]int) {
    if len(*a) > 0 {
        *b = append([]int{(*a)[0]}, *b...)
        *a = (*a)[1:]
        fmt.Println("pb")
    }
}

func pa(a, b *[]int) {
    if len(*b) > 0 {
        *a = append([]int{(*b)[0]}, *a...)
        *b = (*b)[1:]
        fmt.Println("pa")
    }
}

// Sort the remaining 3 elements in stack A
func sortThree(a []int) {
    if a[0] > a[1] {
        sa(a)
    }
    if a[1] > a[2] {
        ra(a)
        if a[0] > a[1] {
            sa(a)
        }
        rra(a)
    }
    if a[0] > a[1] {
        sa(a)
    }
}

func sortFive(a []int) {
    b := []int{}

    // Push the smallest 2 elements to stack B
    for i := 0; i < 2; i++ {
        minIndex := 0
        for j := 1; j < len(a); j++ {
            if a[j] < a[minIndex] {
                minIndex = j
            }
        }
        for minIndex > 0 {
            if minIndex == 1 {
                sa(a)
                minIndex--
            } else {
                ra(a)
                minIndex--
            }
        }
        pb(&a, &b)
    }

    // Sort the remaining 3 elements in stack A
    sortThree(a)

    // Push the elements from stack B back to stack A
    pa(&a, &b)
    pa(&a, &b)

    // Final adjustments to ensure the stack is sorted
    if a[0] > a[1] {
        sa(a)
    }
}


func main() {
    a := []int{11, 2, 3, 94, 50}
    sortFive(a)
    fmt.Println(a) // Output should be [1, 2, 3, 4, 5]
}