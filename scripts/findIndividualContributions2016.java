package scripts;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class findIndividualContributions2016 {
    public static void main(String[] args) throws FileNotFoundException {
        File HillaryFile = new File("HillaryCommittees.txt");
        File trumpFile = new File("TrumpCommittees.txt");

        Scanner bsc = new Scanner(HillaryFile);
        Scanner tsc = new Scanner(trumpFile);

        ArrayList<String> trumpCommittees = new ArrayList<>();
        ArrayList<String> HillaryCommittees = new ArrayList<>();
        
        String line = "";
        // Hillary committees
        while (bsc.hasNextLine()){
            line = bsc.nextLine();
            String [] deets = line.split("[|]");
            HillaryCommittees.add(deets[0]);
        }
        //Trump committees
        while (tsc.hasNextLine()){
            line = tsc.nextLine();
            String [] deets = line.split("[|]");
            trumpCommittees.add(deets[0]);
        }

        // Read files for individual donors
        int HillaryDonors = 0;
        int HillaryContributions = 0;

        int trumpDonors = 0;
        int trumpContributions = 0;

        String datapath = "Contributions_by_individuals_2016/itcont.txt";

        File folder = new File(datapath);
        File[] listOfFiles = folder.listFiles();


        
        //Loop through the files for records in 2020
        // int record = 0;

        /*
         * Looking at donations from December 30th 2019 to August 31st 2020
         * 
         */
        // for(int i=1; i<listOfFiles.length-1; i++){
            File file = new File(datapath);
            String s;
            try{
                Scanner sc = new Scanner(file);
                while( sc.hasNextLine()){
                    // record++;
                        line = sc.nextLine();
                        String [] details = line.split("[|]");
                        
                        String committee = details[0];
                        
                        if(trumpCommittees.contains(committee)){
                            trumpDonors = Integer.parseInt(details[14])>0?trumpDonors+1:trumpDonors-1;
                            trumpContributions += Integer.parseInt(details[14]);
                        }
                        else if((HillaryCommittees.contains(committee))|| details[19].contains("EARMARKED FOR HILLARY")){
                            HillaryDonors = Integer.parseInt(details[14])>0?HillaryDonors+1:HillaryDonors-1;
                            HillaryContributions += Integer.parseInt(details[14]);
                        }
                }
            }
            catch (FileNotFoundException e){
                System.out.print(e);
            }
        // }
        System.out.println("Donations in the 2016 election cycle:");
        System.out.printf("Total Hillary Individual donations: %,d %n",HillaryDonors);
        System.out.printf("Total Sum of Contributions to Hillary: $%,d %n", HillaryContributions);
        System.out.printf("Average Contribution: $%,.2f %n", (HillaryContributions*1.0)/(trumpDonors*1.0));

        System.out.println();
        System.out.printf("Total Trump Individual donations: %,d %n",trumpDonors);
        System.out.printf("Total Sum of Contributions to Trump: $%,d %n",trumpContributions);
        System.out.printf("Average Contribution: $%,.2f %n", (trumpContributions*1.0)/(trumpDonors*1.0));



    }
}
