class TopWindow implements Window{
    private PImage proconLogo;
    private GTextField tokenInputForm;
    private GButton tokenEnterButton;
    private gui_client parent;

    TopWindow(gui_client parent){
        this.parent = parent;

        // Load Assets
        proconLogo = loadImage("res/proconlogo.jpeg");

        // Create G4P Instance
        this.tokenInputForm = new GTextField(
            this.parent, 550, 550, 200, 20
        );
        this.tokenEnterButton = new GButton(
            this.parent, 500, 600, 200, 30, "START"
        );

        // Tag Set
        this.tokenInputForm.tag = "TokenInput";
        this.tokenEnterButton.tag = "ClientStart";
    }

    void start(){
        this.tokenInputForm.setVisible(true);
        this.tokenEnterButton.setVisible(true);
    }

    void finish(){
        this.tokenInputForm.setVisible(false);
        this.tokenEnterButton.setVisible(false);
    }

    void draw(){
        background(255);

        // Title Text
        textAlign(CENTER);
        fill(0);
        textSize(40);
        text("Procon30 Battle System", 600, 200);
        text("GUI Client", 600, 250);

        // Title Logo
        imageMode(CENTER);
        image(this.proconLogo, 600, 400);

        // TokenInputForm
        textSize(20);
        text("TOKEN:", 500, 568);
    }

    // Button
    void handleButtonEvents(GButton button, GEvent event){
        if(TOKEN.length() > 0){
            println(TOKEN);
            windows.put("BattleSelect", new BattleSelectWindow(this.parent));
            switchWindow("BattleSelect");
        }
    }

    // TextFieled
    void handleTextEvents(GEditableTextControl textcontrol, GEvent event){
        TOKEN = textcontrol.getText();
    }

    // Key Events
    void keyPressed(){}
    void keyReleased(){}
}