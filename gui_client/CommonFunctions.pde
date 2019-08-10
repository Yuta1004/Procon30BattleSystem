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

String getNowTime(){
    String hour = nf(hour(), 2);
    String minute = nf(minute(), 2);
    String second = nf(second(), 2);
    return hour + ":" + minute + ":" + second;
}