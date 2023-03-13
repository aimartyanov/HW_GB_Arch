public class Main
{
    public static void main(String[] args) throws Exception {
        String [] list = {"name:Ivanov, country:Russia, city:Moscow, age:null"};
        StringBuilder resultSelect = LineInList(list[0]);
        System.out.println(resultSelect);
    }
    public static StringBuilder LineInList(String line) {
        String line1 = line.replace("{", "");
        String line2 = line1.replace("}", "");
        String line3 = line2.replaceAll("\"", "");
        System.out.println(line3);
        StringBuilder result = new StringBuilder("select * from students where ");

        String [] arrayData = line3.split(", ");
        for (int i =0; i < arrayData.length; i++) {
            String[] arrData = arrayData[i].split(":");
            if(!arrData[1].equals("null")) {
                if (i != 0) {
                    result.append(", ");
                    result.append(arrData[0]);
                    result.append(" = ");
                    result.append(arrData[1]);
                } else {
                    result.append(arrData[0]);
                    result.append(" = ");
                    result.append(arrData[1]);
                }
            }
        }
        return result;
    }
}