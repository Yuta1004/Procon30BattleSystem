import g4p_controls.*;
import http.requests.*;

String TOKEN = "";
String HOST = "http://localhost:16000/procon30-battle-api";

TopWindow topWindow;


void setup(){
    size(800, 800);
    
    topWindow = new TopWindow(this);
}

void draw(){
    topWindow.topWindowDraw();
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