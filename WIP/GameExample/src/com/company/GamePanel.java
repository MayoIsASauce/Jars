package com.company;

import javax.crypto.Mac;
import javax.sound.sampled.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.imageio.ImageIO;
import javax.swing.Timer;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.*;
import java.util.List;

public class GamePanel extends JPanel implements ActionListener
{

    private Timer timer;

    private int ego_dx;
    private int ego_dy;
    private int ego_x;
    private int ego_y;
    private int ego_health;

    private boolean[] going_up = {false, false, false, false, false};

    private int cam_rot = 0;
    private final int max_rot = -3138;
    private final int min_rot = 0;

    private int distance = 0;
    private final int max_distance = 50;

    BufferedImage overlay;
    Clip walking_sfx;

    _dialogHandler dialog = new _dialogHandler();
    boolean fetch_dialog = false;
    boolean cancel_dialog = true;
    boolean show_dialog = true;
    String current_line;

    private _objects[] all_objects = {
            new _objects("rock.gif", new Point(1000, 150), new Dimension(200, 200)),
            new _objects("bloodrush.png", new Point(2600, 150), new Dimension(200, 200)),
    };

    // ok so im too lazy to type this now but i think i got it || DOESNT WORK FUCK YOU

    // if x1 < 145 && !x1 <= 0 then we know to start going up
    // BUT
    // we can check whether y1 equals y2 then go down? ig i never finished writing

    private void setOverlay() {
        try {
         overlay = ImageIO.read(Objects.requireNonNull(getClass().getResource("BEST_OVER.png")));
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    private void setWalking_sfx() {
        try {
            AudioInputStream a_in = AudioSystem.getAudioInputStream(new File(Objects.requireNonNull(getClass().getResource("walking.wav")).toURI()).getAbsoluteFile());
            walking_sfx = AudioSystem.getClip();
            walking_sfx.open(a_in);
        } catch (UnsupportedAudioFileException | IOException | LineUnavailableException | URISyntaxException e) {
            e.printStackTrace();
        }
    }

    public class _dialogHandler {
        private List<String> queued = new ArrayList<>();
        public int amount_passed = 0;

        public void add_to_queue(String line) {
            queued.add(line);
        }
        public void add_to_queue(String[] lines) {
            queued.addAll(Arrays.asList(lines));
        }
        public String get_next() {
            String next = queued.get(0);
            amount_passed--;
            queued.remove(0);
            return next;
        }
    }

    public class _objects {
        public Image sprite;
        public Point location;
        public Dimension size;
        public boolean hidden = false;

        public _objects(String path_to_image, Point location, Dimension size) {
            sprite = new ImageIcon(Objects.requireNonNull(getClass().getResource(path_to_image))).getImage().getScaledInstance(size.width, size.height, Image.SCALE_DEFAULT);
            this.location = location;
            this.size = size;
        }
    }

    private void start_walking() {
        walking_sfx.loop(100);
        walking_sfx.start();
    }
    private void stop_walking() {
        walking_sfx.stop();
    }

    public GamePanel()
    {
        ego_x = 400;
        ego_y = 300;
        ego_dx = 0;
        ego_dy = 0;
        ego_health = 100;
        timer = new Timer(10, this);
        timer.start();
        setFocusable(true);
        requestFocusInWindow();
        TAdapter keyhandler = new TAdapter();
        addKeyListener(keyhandler);
        setOverlay();
        setWalking_sfx();
        dialog.add_to_queue(new String[] {"Yo, it's me the rock", "...", "So you're (insert name here)", "Nice to meet you (insert name here)", "What's that you want my autograph", "...",
                "Sure kid, but first you have to get me my BloodRush™", "It's the protein powder behind you", "Get me that and I'll give you whatever"});
        current_line = dialog.get_next();


    }

    @Override
    public void actionPerformed(ActionEvent e) {
        // THIS CODE IS RUN EVERY 10 MS when the "timer" goes off
        // THIS IS THE GAME LOOP
        cam_rot += -ego_dx;
        distance += ego_dy;

        if (ego_dy != 0 || ego_dx != 0) cancel_dialog = true;
        else cancel_dialog = false;

        if (ego_dy != 0 || ego_dx != 0) start_walking();
        else stop_walking();

        if (distance > max_distance)
            distance = max_distance;
        if (distance < -max_distance)
            distance = -max_distance;

        if (cam_rot < max_rot)
            cam_rot = min_rot;
        if (cam_rot > min_rot)
            cam_rot = max_rot;

        repaint();
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        Dimension screen_info = getSize();
        int half_width = screen_info.width/2;
        int margin = 50;
        int max_offset = 130;
        g.setFont(Font.getFont("Arial"));

        Polygon poly;

        for (int i = 0; i < 5; i++) { // FOREACH WALL

            switch (i) {
                case 1:
                    g.setColor(Color.green);
                    break;
                case 2:
                    g.setColor(Color.RED);
                    break;
                case 3:
                    g.setColor(Color.MAGENTA);
                    break;
                case 4:
                case 0:
                default:
                    g.setColor(Color.BLUE);
                    break;
            }

            poly = new Polygon();
            int poly_x = (screen_info.width * i) + cam_rot;
            int poly_x2 = screen_info.width+(screen_info.width*i)+cam_rot;

            /*
            int state = 0;
            if (poly_x <= 0 || (poly_x > half_width-30 && poly_x < half_width+30) && state != 1) {
                state = 0; // GO DOWN
            } else if ((poly_x > half_width-30 && poly_x < half_width+30) && state == 2) {
                state = 1; // GO UP
            }
            */


            // opposite down
//            offset_y1 = margin + Math.abs(cam_rot);
//            offset_y2 = margin + cam_rot;
//            if (offset_y1 > 185) offset_y1 = 185;
//            if (offset_y2 < margin) offset_y2 = margin;


            // To bring the offset up - instead of +
            int offset_y1;
            int offset_y2;
            if ((poly_x >= -30 && poly_x <= 30)
                    || (poly_x >= screen_info.width-30 && poly_x <= screen_info.width+30)
                    || ((poly_x2 >= -30 && poly_x2 <= 30))
                    || (poly_x2 >= screen_info.width-30 && poly_x2 <= screen_info.width+30)) {
                offset_y1 = margin;
                offset_y2 = margin;
            }
            else if (poly_x < 0) {
                offset_y1 = margin;
                offset_y2 = 185;
            } else {
                offset_y1 = 185;
                offset_y2 = margin;
            }

            poly.addPoint(poly_x, offset_y1 +distance);
            poly.addPoint(poly_x2, offset_y2 +distance);
            poly.addPoint(poly_x2, screen_info.height-margin-distance);
            poly.addPoint(poly_x, screen_info.height-margin-distance);
            g.fillPolygon(poly);

            if (i == 1) {
                g.setColor(Color.BLACK);
                g.drawString("x1: " + poly_x, 0, 60);
            }
        }


        for (_objects obj : all_objects) {
            g.drawImage(obj.sprite, (obj.location.x+cam_rot), (obj.location.y), null);
        }

        g.drawImage(overlay, 0, -20, null);
        g.setColor(Color.BLACK);

//        if (show_dialog) {
//            Polygon temp = new Polygon();
//
//            temp.addPoint(100, 350);
//            temp.addPoint(700, 350);
//            temp.addPoint(700, 450);
//            temp.addPoint(100, 450);
//
//            g.fillPolygon(temp);
//
//            g.setColor(Color.WHITE);
//            g.setFont(new Font("Verdana", Font.BOLD, 18));
//            g.drawString(current_line, 120, 390);
//        }

        g.setFont(new Font("Arial", Font.PLAIN, 11));
        g.setColor(Color.BLACK);
        g.drawString("cam_rot: "+cam_rot, 0, 20);
        g.drawString("distance: "+distance, 0, 40);

    }


    private class TAdapter extends KeyAdapter {

        @Override
        public void keyReleased(KeyEvent e) {
            if(e.getKeyCode() == KeyEvent.VK_LEFT)
            {
                ego_dx=0;
            }
            if(e.getKeyCode() == KeyEvent.VK_RIGHT)
            {
                ego_dx=0;
            }
            if(e.getKeyCode() == KeyEvent.VK_UP)
            {
                ego_dy=0;
            }
            if(e.getKeyCode() == KeyEvent.VK_DOWN)
            {
                ego_dy=0;
            }
        }

        @Override
        public void keyPressed(KeyEvent e) {
            if (e.getKeyCode() == KeyEvent.VK_E)
            {
                current_line = dialog.get_next();
            }
            int look_speed = 5;
            if(e.getKeyCode() == KeyEvent.VK_LEFT)
            {
                ego_dx=-look_speed;
            }
            if(e.getKeyCode() == KeyEvent.VK_RIGHT)
            {
                ego_dx= look_speed;
            }
            if(e.getKeyCode() == KeyEvent.VK_UP)
            {
               ego_dy=-look_speed;
            }
            if(e.getKeyCode() == KeyEvent.VK_DOWN)
            {
              ego_dy= look_speed;
            }
        }
    }
}
