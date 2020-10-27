package scripts;

import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class FindCommitteesContributions2016{
    public static void main(String[]args) throws IOException {
        String datapath = "contributions_by_individuals/by_date/";
        ArrayList <String>committees = new ArrayList<>();

        String TrumpID = "P80001571";
        String HillaryID = "P00003392";

        File file = new File("contribution_from_committees_to_candidates.txt");
        Scanner sc = new Scanner(file);

        ArrayList<String> Committees4Trump = new ArrayList<>();
        ArrayList<String> Committees4Hillary = new ArrayList<>();
        int trumpTotal = 0;
        int HillaryTotal = 0;
        int HillaryContributions = 0;
        int trumpContributions = 0;

        //Committees4Hillary.add("C00703975");
        //Committees4Trump.add("C00580100");

        // FileWriter trumpCommitteesFile = new FileWriter("TrumpCommittees.txt");
        // FileWriter HillaryCommitteesFile = new FileWriter("HillaryCommittees.txt");

        String line = "";
        while(sc.hasNextLine()){
            line = sc.nextLine();
            String [] details = line.split("[|]");
            // System.out.println(details.length);
            if(details[16].equals(TrumpID)){
                trumpContributions += 1;
                trumpTotal += Integer.parseInt(details[14]);
                // if(!Committees4Trump.contains(details[0])){
                //     //Add Committee to list and append committee details to file
                //     Committees4Trump.add(details[0]);
                //     trumpCommitteesFile.append(details[0]+"|"+ details[7]+"\n");
                // }
            }
            else if(details[16].equals(HillaryID)){
                HillaryContributions += 1;
                HillaryTotal += Integer.parseInt(details[14]);
                // if(!Committees4Hillary.contains(details[0])){
                //     //Add Committee to list and append committee details to file
                //     Committees4Hillary.add(details[0]);
                //     HillaryCommitteesFile.append(details[0]+"|"+ details[7]+"\n");
                // }
            }
        }
        System.out.println("Contributions to Candidates from other Committees (2019 - 2020)\n");
        System.out.printf("Total sum of contributions for Hillary: $%,d %n", HillaryTotal);
        System.out.printf("Total number of contributions for Hillary: %,d %n", HillaryContributions);

        System.out.println();
        System.out.printf("Total sum of contributions for Trump: $%,d %n", trumpTotal);
        System.out.printf("Total number of contributions for Trump: %,d %n", trumpContributions);

        // trumpCommitteesFile.close();
        // HillaryCommitteesFile.close();

        // Read the files
        /*
        File folder = new File(datapath);
        File[] listOfFiles = folder.listFiles();


        
        //Loop through the files for records in 2020
        // int record = 0;
        for(int i=8; i<listOfFiles.length; i++){
            File file = new File(datapath+listOfFiles[i].getName());
            String s;
            try{
                Scanner sc = new Scanner(file);
                while( sc.hasNextLine()){
                    // record++;
                        String line = sc.nextLine();
                        String committee = line.substring(0,9);
                        // System.out.println(record);
                        if(!committees.contains(committee)){
                            committees.add(committee);
                            System.out.println(committee);
                            System.out.println(committees.size());
                        }
                }
            }
            catch (FileNotFoundException e){
                System.out.print(e);
            }
        }
        */

    }
}