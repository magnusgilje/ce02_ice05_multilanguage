
class Circle {  
    Radius: number;  
    constructor(Radius: number) {  
        this.Radius = Radius;  
    }  
    Area() {  
        return Math.PI * this.Radius * this.Radius;  
    }  
    Perimeter() {  
        return 2 * Math.PI * this.Radius;  
    }  
    Summary() {

        var formatted = `area=${this.Area()}, perimeter=${this.Perimeter()}`;
        return formatted;
    }
}  

const args = require('yargs').argv;

var radius = args.radius
var circle = new Circle(radius);  

console.log(circle.Summary())