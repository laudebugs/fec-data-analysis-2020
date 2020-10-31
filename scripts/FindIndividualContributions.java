package scripts;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class findIndividualContributions {
    public static void main(String[] args) throws FileNotFoundException {
        File bidenFile = new File("candidateInfo/BidenCommittees.txt");
        File trumpFile = new File("candidateInfo/TrumpCommittees.txt");

        Scanner bsc = new Scanner(bidenFile);
        Scanner tsc = new Scanner(trumpFile);

        ArrayList<String> trumpCommittees = new ArrayList<>();
        ArrayList<String> bidenCommittees = new ArrayList<>();
        
        String line = "";
        // Biden committees
        while (bsc.hasNextLine()){
            line = bsc.nextLine();
            String [] deets = line.split("[|]");
            bidenCommittees.add(deets[0]);
        }
        //Trump committees
        while (tsc.hasNextLine()){
            line = tsc.nextLine();
            String [] deets = line.split("[|]");
            trumpCommittees.add(deets[0]);
        }

        // Read files for individual donors
        int bidenDonors = 0;
        int bidenContributions = 0;

        int trumpDonors = 0;
        int trumpContributions = 0;

        String datapath = "indiv20/itcont.txt";

        File folder = new File(datapath);

        File file = new File(datapath);
        try{
            Scanner sc = new Scanner(file);
            while( sc.hasNextLine()){
                    line = sc.nextLine();
                    String [] details = line.split("[|]");
                    
                    String committee = details[0];
                    String earmark = details[15];
                    if(trumpCommittees.contains(committee) || trumpCommittees.contains(earmark)){
                        trumpDonors = Integer.parseInt(details[14])>0?trumpDonors+1:trumpDonors-1;
                        trumpContributions += Integer.parseInt(details[14]);
                    }
                    else if((bidenCommittees.contains(committee))|| bidenCommittees.contains(earmark)){
                        bidenDonors = Integer.parseInt(details[14])>0?bidenDonors+1:bidenDonors-1;
                        bidenContributions += Integer.parseInt(details[14]);
                        
                    }
                    
            }
        }
        catch (FileNotFoundException e){
            System.out.print(e);
        }
        
        System.out.println("Donations from 2019 through to August 31st 2020:");
        System.out.printf("Total Biden Individual donations: %,d %n",bidenDonors);
        System.out.printf("Total Sum of Contributions to Biden: $%,d %n", bidenContributions);
        System.out.printf("Average Contribution: $%,.2f %n", (bidenContributions*1.0)/(bidenDonors*1.0));
        System.out.println();
        System.out.printf("Total Trump Individual donations: %,d %n",trumpDonors);
        System.out.printf("Total Sum of Contributions to Trump: $%,d %n",trumpContributions);
        System.out.printf("Average Contribution: $%,.2f %n", (trumpContributions*1.0)/(trumpDonors*1.0));



    }
}
