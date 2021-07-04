# SOS

## Write-up

1. Morse code decoding, we'll get a text which contains `E`, `T` and `BREAK`
2. Replace `BREAK` with a line break, `E` with `0` and `T` with `1`.
3. The resulting file is an image in ppm format of type 1.
4. After counting the number of lines and columns (108 x 108), we add the header:
```
P1
108 108
```
5. Open the image in gimp for example, read the barcode using your phone or upload
the image to a website such as zxing.

## Flag

`shellmates{1_l0v3_b4rc0d3es_4nd_1_l0v3_d3_4zt3c_:)}`
