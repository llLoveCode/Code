public class SpeciesFirstTryDemo {
    public static void main(String[] args)
    {
        SpeciesFirstTry speciesofthenmonths = new SpeciesFirstTry();
        int futurePopulation;
        
        System.out.println("Enter data on the Species of the month:");
        speciesofthenmonths.readInput();
        speciesofthenmonths.WriteOutput();

        futurePopulation = speciesofthenmonths.populationIn();
        System.out.println("In ten years the population will be "+ futurePopulation);

        speciesofthenmonths.name = "kilngon ox";
        speciesofthenmonths.population = 10;
        speciesofthenmonths.growthRate = 15;

        speciesofthenmonths.WriteOutput();
        System.out.println("In ten years the population will be "+ speciesofthenmonths.populationIn());

    }
}
