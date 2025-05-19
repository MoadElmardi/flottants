use tfhe::prelude::*;
use tfhe::{generate_keys, set_server_key, ConfigBuilder, FheInt64};
//use std::time::{Duration, Instant};

pub fn main() -> Result<(), Box<dyn std::error::Error>> {
    //let now = Instant::now();
    let scale: f64 = 1e9;
    let config = ConfigBuilder::default().build();
    let (client_key, server_keys) = generate_keys(config);
    set_server_key(server_keys);

    let a = 1.23451256;
    let a_encode: i64 = (a * scale).round() as i64;
    let b = 6.78912312;
    let b_encode: i64 = (b * scale).round() as i64;

    let ctxt_a = FheInt64::encrypt(a_encode, &client_key);
    let ctxt_b = FheInt64::encrypt(b_encode, &client_key);

    let ctxt_result = &ctxt_a / &ctxt_b;

    let scaled_res: i64 = ctxt_result.decrypt(&client_key);
    let _result: f64 = (scaled_res as f64) / scale;
    //let duration = now.elapsed();

    Ok(())
}
