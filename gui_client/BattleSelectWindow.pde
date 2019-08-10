class BattleSelectWindow implements Window{
    BattleSelectWindow(){}
    void start(){}
    void finish(){}

    void draw(){
        background(255);

        // Window Title
        fill(0);
        textSize(40);
        textAlign(CENTER);
        text("Battle Select", 600, 150);
    }

    /* G4P functions */
    void handleButtonEvents(GButton button, GEvent event){}
    void handleTextEvents(GEditableTextControl textcontrol, GEvent event){}

    /* Key events */
    void keyPressed(){}
    void keyReleased(){}
}