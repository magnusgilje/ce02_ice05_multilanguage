package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
)

func area(radius float32) float32 {
	return math.Pi * radius * radius
}

func perimeter(radius float32) float32 {
	return 2.0 * math.Pi * radius
}

func summary(radius float32) string {
	area := area(radius)
	perimeter := perimeter(radius)

	result := fmt.Sprintf("area=%0.2f perimeter=%0.2f", area, perimeter)
	return result
}

func main() {

	value, err := strconv.ParseFloat(os.Args[1], 32)
	if err == nil {
		radius := float32(value)
		fmt.Println(summary(radius))
	}
}
