import java.util.*;
public class SpeciesFirstTry {
    public String name;
    public int population;
    public double growthRate;

    public void readInput()
    {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("what is the species' name?");
        name = keyboard.nextLine();

        System.out.println("what is the population of the species?");
        population = keyboard.nextInt();
        while(population < 0){
            System.out.println("Population cannot be negtive.");
            System.out.println("Reenter population:");
            population = keyboard.nextInt();            
        }
        System.out.println("Enter growth rate (percent increase per year):");
        growthRate = keyboard.nextDouble();        
    }

    public void WriteOutput()
    {
        System.out.println("Name = " + name);
        System.out.println("Population = " + population);
        System.out.println("Growth rage = " + growthRate + "%");
    }
    public int populationIn()
    {
        double populationAmount = population;
        int count = 10;
        while((0 < count)&&(0 < populationAmount))
        {
            populationAmount = (populationAmount + (growthRate/100)*populationAmount);
            count--;
        }
        if(0 < populationAmount)
        {
            return (int)populationAmount;
        }
        else
        {
            return 0;
        }
    }
}
