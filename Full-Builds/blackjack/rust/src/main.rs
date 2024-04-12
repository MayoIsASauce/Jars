use serde_json::from_str;
use serde::{Deserialize, Serialize};

use crate::{definitions::drawable_t, definitions::event_t, python::{recv_python, send_python}};

mod python;
mod utils;
mod definitions;


fn main() {
    let mut child = python::start_python();

    let _ = send_python(&mut child, "800, 600".to_string());

    let player = drawable_t {xy: (20f32, 20f32), size: (50f32, 50f32), 
                                        color: (255, 0, 0)};

    loop {
        let mut closing: bool = false;
    
        let c = recv_python(&mut child);
        if c.is_ok() {
            let data = c.unwrap();

            let events: Vec<event_t> = serde_json::from_str(&data).expect("failed to deserialize");
            for event in events {
                if event.name == 256 {
                    println!("got end signal");
                    closing = true;
                    break;
                }
                println!("{}", event.name);
            }
        }

        let _ = send_python(&mut child, serde_json::to_string(&player).expect("couldnt serialize"));
        if closing == true { break; }
    }

    let e_code = child.wait().unwrap();
    println!("\n{}", e_code.to_string());
}
