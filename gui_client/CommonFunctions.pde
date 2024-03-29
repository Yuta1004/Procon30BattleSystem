ArrayList<ArrayList<Integer>> convertJSONArray2d(JSONArray target){
    ArrayList<ArrayList<Integer>> retArray = new ArrayList<ArrayList<Integer>>();
    for(int idx_i = 0; idx_i < target.size(); ++ idx_i){
        JSONArray jsonArrayItem = target.getJSONArray(idx_i);
        retArray.add(new ArrayList<Integer>());
        for(int idx_j = 0; idx_j < jsonArrayItem.size(); ++ idx_j){
            retArray.get(idx_i).add(jsonArrayItem.getInt(idx_j));
        }
    }
   return retArray;
}

String formatDate(int hour, int minute, int second){
    String hourStr = nf(hour, 2);
    String minuteStr = nf(minute, 2);
    String secondStr = nf(second, 2);
    return hourStr + ":" + minuteStr + ":" + secondStr;
}

int signum(int value){
    if(value > 0) return 1;
    if(value < 0) return -1;
    return 0;
}

void displayErrorDialog(String message){
    G4P.showMessage(this, message, "Error", G4P.ERROR);
}