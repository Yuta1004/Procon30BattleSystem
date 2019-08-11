/* Libraries */
import g4p_controls.*;

/* Const Values */
String TOKEN = "";
String HOST = "http://localhost:16000/procon30-battle-api";

/* Var Values */
HashMap<String, Window> windows;
HashMap<Integer, Battle> battleList;
String nowViewingWindowID;

/* Processing Standard Functions */
void setup(){
    frameRate(15);
    size(1200, 800);

    nowViewingWindowID = "";
    windows = new HashMap<String, Window>();
    windows.put("Top", new TopWindow(this));
    windows.get("Top").finish();
    switchWindow("Top");

    battleList = new HashMap<Integer, Battle>();
}

void draw(){
    windows.get(nowViewingWindowID).draw();
}

/* G4P Handlers */
// Button
public void handleButtonEvents(GButton button, GEvent event){
    windows.get(nowViewingWindowID).handleButtonEvents(button, event);
}

// TextFieled
public void handleTextEvents(GEditableTextControl textcontrol, GEvent event){
    windows.get(nowViewingWindowID).handleTextEvents(textcontrol, event);
}

// Key Events
void keyPressed(){
    windows.get(nowViewingWindowID).keyPressed();
}

void keyReleased(){
    windows.get(nowViewingWindowID).keyReleased();
}

/* Other Functions */
boolean switchWindow(String moveToWindowID){
    if(windows.containsKey(moveToWindowID)){
        if(!"".equals(nowViewingWindowID))
            windows.get(nowViewingWindowID).finish();
        windows.get(moveToWindowID).start();
        nowViewingWindowID = moveToWindowID;
        return true;
    }
    return false;
}