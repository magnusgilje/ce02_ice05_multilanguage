using System;
namespace Circle
{class Circle
{
    public Circle(float Radius)
    {
        this.Radius = Radius;
    }

    private float Radius {get;set;}


    public string Summary()
    {
        return String.Format("area={0:0.00}, perimeter={1:0.00}", this.Area(), this.Perimeter());
    }

    private float Area()
    {
        return (float)Math.PI * Radius * Radius;
    }
    
    private float Perimeter()
    {
        return (float)Math.PI * 2.0f * Radius;
    }
}
}