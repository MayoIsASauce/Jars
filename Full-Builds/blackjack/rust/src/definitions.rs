use serde_json::value::Value;
use serde::{Serialize, Deserialize};


#[allow(non_camel_case_types)]
#[derive(Serialize, Deserialize)]
pub struct drawable_t {
    pub xy: (f32, f32),
    pub size: (f32, f32),
    pub color: (u16, u16, u16)
}

#[allow(non_camel_case_types)]
#[derive(Serialize, Deserialize)]
pub struct event_t {
    pub name: i32,
    pub args: Value
}