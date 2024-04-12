use crate::utils;

use std::process::Command;
use std::io::{Error, Read, Write};
use std::process::{Stdio, Child};

pub fn start_python() -> Child {
    Command::new("python3")
        .arg(utils::get_path("python/main.py").to_str().unwrap())
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .spawn()
        .expect("Unable to open python child")
}

#[allow(dead_code)]
pub fn send_python(python: &mut Child, content: String) -> Result<(), Error>{
    if let Some(ref mut stdin) = python.stdin {
        match stdin.write_all((content + "\n").as_bytes()) {
            Ok(_) => (),
            Err(err) => return Err(err),
        }
        stdin.flush().expect("Unable to flush python stdin");
    }
    Ok(())
}

#[allow(dead_code)]
pub fn recv_python(python: &mut Child) -> Result<String, Error> {
    let mut output = String::new();
    if let Some(ref mut stdout) = python.stdout {
        loop {
            let mut buffer = [0; 1];
            match stdout.read_exact(&mut buffer) {
                Ok(_) => {
                    let byte = buffer[0];
                    if byte == b'\n' {
                        break;
                    }
                    output.push(byte as char);
                },
                Err(err) => return Err(err),
            }
        }
    }
    Ok(output)
}