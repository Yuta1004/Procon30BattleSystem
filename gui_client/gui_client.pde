/* Libraries */
import g4p_controls.*;
import http.requests.*;

/* Const Values */
String TOKEN = "";
String HOST = "http://localhost:16000/procon30-battle-api";

/* Var Values */
HashMap<String, Window> windows;
String nowViewingWindowID;

/* Processing Standard Functions */
void setup(){
    size(800, 800);

    nowViewingWindowID = "Top";
    windows = new HashMap<String, Window>();
    windows.put("Top", new TopWindow(this));
}

void draw(){
    windows.get(nowViewingWindowID).draw();
}

/* G4P Handlers */
// Button
public void handleButtonEvents(GButton button, GEvent event){
    if("ClientStart".equals(button.tag)){
        if(TOKEN.length() > 0){
            println(TOKEN);
        }
    }
}

// TextFieled
public void handleTextEvents(GEditableTextControl textcontrol, GEvent event){
    if("TokenInput".equals(textcontrol.tag)){
        TOKEN = textcontrol.getText();
    }
}

/* Other Functions */
boolean switchWindow(String moveToWindowID){
    if(windows.containsKey(moveToWindowID)){
        windows.get(nowViewingWindowID).finish();
        nowViewingWindowID = moveToWindowID;
        windows.get(nowViewingWindowID).start();
        return true;
    }
    return false;
}