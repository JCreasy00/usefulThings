// this is just a very simply and probably not very efficient while loop that takes in numbers until -1 is inputted and then
// the program outputs the average of those numbers

public class averageCalc {
  public static void main(String[] args) {
    final int SENTINEL = -1;
		Scanner myObj = new Scanner(System.in);
		int numOfScores = 0;
		double sumOfScores = 0;
		
		System.out.print("Gathering you Exam Scores...You can type -1 to quit...Whats your first score?: ");
		int currentScore = myObj.nextInt();
		
		while (currentScore != SENTINEL) {
			numOfScores++;
			sumOfScores += currentScore;
			
			System.out.print("Next Score?: ");
			currentScore = myObj.nextInt();
		}
		myObj.close();
		System.out.println("The average is " + sumOfScores/numOfScores);
  }
}
