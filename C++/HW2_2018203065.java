import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class HW2_2018203065 {
	private static List<Integer> Subset = new ArrayList<>();
	private static List<Integer> OtherSubset = new ArrayList<>();
	private static long[][] count = null;
	private static int PartitionExist=0;
	private static void MakingTwoOfSubsets(int [] array, int sum, int exist) {
		if(exist == 1 ) {
		//(1) : 두개의 부분집합 ArrayList 생성
		Subset = new ArrayList<>();
		OtherSubset = new ArrayList<>();
		
		//(2) : 변수 값 초기화
		int n = array.length;
    	int arraynum = n - 1;
        int sumnum = sum;
        
        //(3) : 첫번째 배열 값 대입
        while (arraynum != 0) {
            if (count[arraynum][sumnum] != count[arraynum - 1][sumnum]) {
                Subset.add(array[arraynum]);
                sumnum -= array[arraynum];
            }
            arraynum--;
        }
        if (sumnum > 0) {
            Subset.add(array[arraynum]);
        }
        //(4) : 두번째 배열 값 대입
        for (int i =0;i<n;i++) {
            if (!Subset.contains(array[i])) {
                OtherSubset.add(array[i]);
            }
        }
        
	}}
	
	
	private static void PrintTwoOfSubsets(int[] array,int sum,int exist) {
		if(exist == 1 ) {
		//(1) : 첫 번째 Subset 출력
        System.out.print("{");
            for (int i = 0; i < Subset.size(); i++) {
                System.out.print(Subset.get(i));
                if (i != Subset.size() - 1) {
                    System.out.print(",");
                }
            }
            System.out.print("} , ");
            

          //(2) : 두 번째 Subset 출력 
            System.out.print("{");
            for (int i = 0; i < OtherSubset.size(); i++) {
                System.out.print(OtherSubset.get(i));
                if (i != OtherSubset.size() - 1) {
                    System.out.print(",");
                }
            }
            System.out.println("}");
    }
	}
	
    private static void countSubsetSum(int[] array, int sum) {
    	int n = array.length;
        if (sum <= 0 || array.length == 0  ) {
            return;
        }
        
        //Making Array : [배열의 크기] [원하는 합+1] 으로 이차원 배열 생성
        count = new long[n][sum + 1];
        //Boundary Condition(1) : 모든 원소들은 합 0을 만들 수 있기 때문에 1로 초기화
        for (int i = 0; i < n; i++) {
            count[i][0] = 1;
        }
        //Recursion1 : 첫번째 원소가 sum의 값이라면 1 넣기
        for (int j = 0; j <= sum; j++) {
        	
            if (array[0] == j) {
                count[0][j] = 1;
            }
        }
        //Recursion2 : 첫번째 원소가 sum의 값이 아니라면
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= sum; j++) {

               
                //(1) : 배열원소보다 sum이 더 크거나 같은 경우, 배열원소의 전의 원소가 sum-array[i]을 만족하고 있는지 확인하기
            	//      만족한다면, 값을 더해준다. 
                if (j - array[i] >= 0) {
                    count[i][j] += count[i - 1][j - array[i]];
                } 
                //모든 경우들은 배열원소의 전원소가 sum을 만날 때의 값을 더해준다
                count[i][j] += count[i - 1][j];
            }
        }
        
        //총 부분집합의 개수 출력하기
        long coun = count[n - 1][sum] / 2;
        PartitionExist=0;
        if(coun != 0) {
        PartitionExist = 1;
        }
        if(coun > Integer.MAX_VALUE || coun < 0 ){
            System.out.println("NUMEROUS");
        } else {
            System.out.println(coun);
        }
        return;
       }
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        Scanner scanner = new Scanner(System.in);
        while (true) {
        	//(1) 입력 : n, array원소
            String N = scanner.nextLine();
            if (N.equals("EOI")) {
                break;
            }
            int n = Integer.parseInt(N);
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = scanner.nextInt();
            }
            
            //(2) partition할 same sum 구하기
            int sum = 0;
            for (int i = 0; i < arr.length; i++) {
                sum += arr[i];
            }
            if(sum%2 == 0) {
            //(3) Partition 순서쌍 구하기
            countSubsetSum(arr, sum / 2);

            //(4) Partition 존재시, 부분집합 순서쌍 만들기 출력하기
            if(PartitionExist == 1) {            
            	MakingTwoOfSubsets(arr,sum / 2,PartitionExist);
            	PrintTwoOfSubsets(arr,sum / 2,PartitionExist);
            }
            }
            else {
            	System.out.println("0");
            }
            
            scanner.nextLine();
        }
	}

}
