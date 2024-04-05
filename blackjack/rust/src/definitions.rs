use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
pub struct GameObject {
    pub x: u16,
    pub y: u16,

    pub w: u32,
    pub h: u32,

    pub color: (u8, u8, u8),
}

#[derive(Serialize, Deserialize)]
pub struct Objects {
    pub background: String,
    pub player: GameObject 
}