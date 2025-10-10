use pyo3::prelude::*;
use pyo3::types::PyBytes;
use pyo3::exceptions::PyValueError;


#[pyfunction]
fn rs_py(py: Python, data: &[u8], key: &[u8], nonce: &[u8]) -> PyResult<Py<PyBytes>> {
    if key.len() != 32 {
        return Err(PyValueError::new_err("Key must be 32 bytes (256 bits)"));
    }
    if nonce.len() != 8 {
        return Err(PyValueError::new_err("Nonce must be 8 bytes (64 bits)"));
    }

    let mut key_array = [0u8; 32];
    let mut nonce_array = [0u8; 8];

    key_array.copy_from_slice(key);
    nonce_array.copy_from_slice(nonce);

    println!("SomePrint");

    // let result = aes_ctr(data, &key_array, &nonce_array);

    Ok(PyBytes::new(py, &data).into())
}

#[pymodule]
fn rspy(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rs_py, m)?)?;
    Ok(())
}
