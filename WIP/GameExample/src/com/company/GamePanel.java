package com.company;
import javax.crypto.Mac;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.Random;

public class GamePanel extends JPanel implements ActionListener
{

    private Timer timer;

    private int ego_dx;
    private int ego_dy;
    private int ego_x;
    private int ego_y;
    private int ego_health;

    private int cam_rot = 0;
    private int max_rot = -3138;
    private int min_rot = 0;

    private int distance = 0;
    private int max_distance = 50;
    private int min_distance = -100;

    // ok so im too lazy to type this now but i think i got it

    // if x1 < 145 then we know to start going up
    // BUT
    // we can check whether y1

    private int look_speed = 3;

    private int offset_y1, offset_y2;

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
        System.out.println(getSize().height-50);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        // THIS CODE IS RUN EVERY 10 MS when the "timer" goes off
        // THIS IS THE GAME LOOP
        cam_rot += -ego_dx;
        distance += ego_dy;

        if (distance > max_distance)
            distance = max_distance;
        if (distance < min_distance)
            distance = min_distance;

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

            /*
            int state = 0;
            if (poly_x <= 0 || (poly_x > half_width-30 && poly_x < half_width+30) && state != 1) {
                state = 0; // GO DOWN
            } else if ((poly_x > half_width-30 && poly_x < half_width+30) && state == 2) {
                state = 1; // GO UP
            }
            */


            // To bring the offset up - instead of +
            if (i%2 == 0) {
                offset_y1 = margin + cam_rot;
                offset_y2 = margin + Math.abs(cam_rot);
                if (offset_y1 < margin) offset_y1 = margin;
                if (offset_y2 > 185) offset_y2 = 185;
            } else {
                offset_y1 = margin + Math.abs(cam_rot);
                offset_y2 = margin + cam_rot;
                if (offset_y1 > 185) offset_y1 = 185;
                if (offset_y2 < margin) offset_y2 = margin;
            }

            poly.addPoint(poly_x, offset_y1+distance);
            poly.addPoint(screen_info.width+(screen_info.width*i)+cam_rot, offset_y2+distance);
            poly.addPoint(screen_info.width+(screen_info.width*i)+cam_rot, screen_info.height-margin-distance);
            poly.addPoint((screen_info.width * i) + cam_rot, screen_info.height-margin-distance);
            g.fillPolygon(poly);

            if (i == 1) {
                g.setColor(Color.BLACK);
                g.drawString("x1: " + poly_x, 0, 60);
            }
        }

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
            if (e.getKeyCode() == KeyEvent.VK_SPACE)
            {

            }
            if(e.getKeyCode() == KeyEvent.VK_LEFT)
            {
                ego_dx=-look_speed;
            }
            if(e.getKeyCode() == KeyEvent.VK_RIGHT)
            {
                ego_dx=look_speed;
            }
            if(e.getKeyCode() == KeyEvent.VK_UP)
            {
               ego_dy=-look_speed;
            }
            if(e.getKeyCode() == KeyEvent.VK_DOWN)
            {
              ego_dy=look_speed;
            }
        }
    }
}
