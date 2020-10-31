package scripts;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class careerTypes {
    public static void main(String[] args) throws FileNotFoundException {
        File bidenFile = new File("candidateInfo/HillaryCommittees.txt");
        File trumpFile = new File("candidateInfo/TrumpCommittees.txt");

        Scanner bsc = new Scanner(bidenFile);
        Scanner tsc = new Scanner(trumpFile);

        ArrayList<String> Careers = new ArrayList<>();
        ArrayList<String> bidenContributors = new ArrayList<>();
        ArrayList<String> trumpContributors = new ArrayList<>();

        String bidenCommittee = bsc.nextLine().split("[|]")[0];
        String trumpCommittee = tsc.nextLine().split("[|]")[0];

        // Read the individual contributions file
        
        

        // Read files for individual donors
        int bidenDonors = 0;
        int bidenContributions = 0;

        int trumpDonors = 0;
        int trumpContributions = 0;

        String datapath = "indiv16/itcont.txt";

        
        File file = new File(datapath);
        String line;
        try{
            Scanner sc = new Scanner(file);
            while( sc.hasNextLine()){
                // record++;
                    line = sc.nextLine();
                    String [] details = line.split("[|]");
                    
                    String committee = details[0];
                    
                    if(trumpCommittee.equals(committee)){
                        trumpDonors = Integer.parseInt(details[14])>0?trumpDonors+1:trumpDonors-1;
                        trumpContributions += Integer.parseInt(details[14]);
                    }
                    else if((bidenCommittee.equals(committee))|| details[19].contains("EARMARKED FOR biden")){
                        bidenDonors = Integer.parseInt(details[14])>0?bidenDonors+1:bidenDonors-1;
                        bidenContributions += Integer.parseInt(details[14]);
                    }
            }
        }
        catch (FileNotFoundException e){
            System.out.print(e);
        }
    
        System.out.println("Donations in the 2016 election cycle:");
        System.out.printf("Total biden Individual donations: %,d %n",bidenDonors);
        System.out.printf("Total Sum of Contributions to biden: $%,d %n", bidenContributions);
        System.out.printf("Average Contribution: $%,.2f %n", (bidenContributions*1.0)/(trumpDonors*1.0));

        System.out.println();
        System.out.printf("Total Trump Individual donations: %,d %n",trumpDonors);
        System.out.printf("Total Sum of Contributions to Trump: $%,d %n",trumpContributions);
        System.out.printf("Average Contribution: $%,.2f %n", (trumpContributions*1.0)/(trumpDonors*1.0));



    }
}
