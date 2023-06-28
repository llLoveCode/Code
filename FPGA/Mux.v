module MUX2_1(out,a,b,sel);
    output out;
    input a,b,sel;
    not(sel_,sel);
    and(a1,a,sel_);
    and(b1,b,sel);
    or(out,a1,b1);
endmodule