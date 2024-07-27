	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 14, 0	sdk_version 14, 4
	.globl	_create_stack                   ; -- Begin function create_stack
	.p2align	2
_create_stack:                          ; @create_stack
	.cfi_startproc
; %bb.0:
	mov	x0, #0
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_push                           ; -- Begin function push
	.p2align	2
_push:                                  ; @push
	.cfi_startproc
; %bb.0:
	stp	x20, x19, [sp, #-32]!           ; 16-byte Folded Spill
	.cfi_def_cfa_offset 32
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	.cfi_offset w19, -24
	.cfi_offset w20, -32
	mov	x20, x1
	mov	x19, x0
	mov	w0, #16
	bl	_malloc
	cbz	x0, LBB1_2
; %bb.1:
	str	w20, [x0]
	ldr	x8, [x19]
	str	x8, [x0, #8]
	str	x0, [x19]
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp], #32             ; 16-byte Folded Reload
	ret
LBB1_2:
Lloh0:
	adrp	x0, l_str@PAGE
Lloh1:
	add	x0, x0, l_str@PAGEOFF
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp], #32             ; 16-byte Folded Reload
	b	_puts
	.loh AdrpAdd	Lloh0, Lloh1
	.cfi_endproc
                                        ; -- End function
	.globl	_pop                            ; -- Begin function pop
	.p2align	2
_pop:                                   ; @pop
	.cfi_startproc
; %bb.0:
	stp	x20, x19, [sp, #-32]!           ; 16-byte Folded Spill
	.cfi_def_cfa_offset 32
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	.cfi_offset w19, -24
	.cfi_offset w20, -32
	mov	x8, x0
	ldr	x0, [x0]
	cbz	x0, LBB2_2
; %bb.1:
	ldr	w19, [x0]
	ldr	x9, [x0, #8]
	str	x9, [x8]
	bl	_free
	mov	x0, x19
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp], #32             ; 16-byte Folded Reload
	ret
LBB2_2:
Lloh2:
	adrp	x0, l_str.7@PAGE
Lloh3:
	add	x0, x0, l_str.7@PAGEOFF
	bl	_puts
	mov	w0, #1
	bl	_exit
	.loh AdrpAdd	Lloh2, Lloh3
	.cfi_endproc
                                        ; -- End function
	.globl	_peek                           ; -- Begin function peek
	.p2align	2
_peek:                                  ; @peek
	.cfi_startproc
; %bb.0:
	stp	x29, x30, [sp, #-16]!           ; 16-byte Folded Spill
	.cfi_def_cfa_offset 16
	mov	x29, sp
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	cbz	x0, LBB3_2
; %bb.1:
	ldr	w0, [x0]
	ldp	x29, x30, [sp], #16             ; 16-byte Folded Reload
	ret
LBB3_2:
Lloh4:
	adrp	x0, l_str.8@PAGE
Lloh5:
	add	x0, x0, l_str.8@PAGEOFF
	bl	_puts
	mov	w0, #1
	bl	_exit
	.loh AdrpAdd	Lloh4, Lloh5
	.cfi_endproc
                                        ; -- End function
	.globl	_is_empty                       ; -- Begin function is_empty
	.p2align	2
_is_empty:                              ; @is_empty
	.cfi_startproc
; %bb.0:
	cmp	x0, #0
	cset	w0, eq
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_print_stack                    ; -- Begin function print_stack
	.p2align	2
_print_stack:                           ; @print_stack
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48
	.cfi_def_cfa_offset 48
	stp	x20, x19, [sp, #16]             ; 16-byte Folded Spill
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	.cfi_offset w19, -24
	.cfi_offset w20, -32
	cbz	x0, LBB5_3
; %bb.1:
	mov	x19, x0
Lloh6:
	adrp	x20, l_.str.3@PAGE
Lloh7:
	add	x20, x20, l_.str.3@PAGEOFF
LBB5_2:                                 ; =>This Inner Loop Header: Depth=1
	ldr	w8, [x19]
	str	x8, [sp]
	mov	x0, x20
	bl	_printf
	ldr	x19, [x19, #8]
	cbnz	x19, LBB5_2
LBB5_3:
Lloh8:
	adrp	x0, l_str.9@PAGE
Lloh9:
	add	x0, x0, l_str.9@PAGEOFF
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #16]             ; 16-byte Folded Reload
	add	sp, sp, #48
	b	_puts
	.loh AdrpAdd	Lloh6, Lloh7
	.loh AdrpAdd	Lloh8, Lloh9
	.cfi_endproc
                                        ; -- End function
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #64
	.cfi_def_cfa_offset 64
	stp	x22, x21, [sp, #16]             ; 16-byte Folded Spill
	stp	x20, x19, [sp, #32]             ; 16-byte Folded Spill
	stp	x29, x30, [sp, #48]             ; 16-byte Folded Spill
	add	x29, sp, #48
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	.cfi_offset w19, -24
	.cfi_offset w20, -32
	.cfi_offset w21, -40
	.cfi_offset w22, -48
	mov	w0, #16
	bl	_malloc
	mov	x19, x0
	cbz	x0, LBB6_2
; %bb.1:
	mov	w8, #10
	str	w8, [x19]
	str	xzr, [x19, #8]
	b	LBB6_3
LBB6_2:
Lloh10:
	adrp	x0, l_str@PAGE
Lloh11:
	add	x0, x0, l_str@PAGEOFF
	bl	_puts
LBB6_3:
	mov	w0, #16
	bl	_malloc
	cbz	x0, LBB6_5
; %bb.4:
	mov	w8, #20
	str	w8, [x0]
	str	x19, [x0, #8]
	mov	x19, x0
	b	LBB6_6
LBB6_5:
Lloh12:
	adrp	x0, l_str@PAGE
Lloh13:
	add	x0, x0, l_str@PAGEOFF
	bl	_puts
LBB6_6:
	mov	w0, #16
	bl	_malloc
	cbz	x0, LBB6_17
; %bb.7:
	mov	w8, #30
	str	w8, [x0]
	str	x19, [x0, #8]
	mov	x19, x0
	cbz	x19, LBB6_18
LBB6_8:
Lloh14:
	adrp	x20, l_.str.3@PAGE
Lloh15:
	add	x20, x20, l_.str.3@PAGEOFF
	mov	x21, x19
LBB6_9:                                 ; =>This Inner Loop Header: Depth=1
	ldr	w8, [x21]
	str	x8, [sp]
	mov	x0, x20
	bl	_printf
	ldr	x21, [x21, #8]
	cbnz	x21, LBB6_9
; %bb.10:
Lloh16:
	adrp	x0, l_str.9@PAGE
Lloh17:
	add	x0, x0, l_str.9@PAGEOFF
	bl	_puts
	cbz	x19, LBB6_19
; %bb.11:
	ldr	x20, [x19, #8]
	ldr	w21, [x19]
	mov	x0, x19
	bl	_free
	str	x21, [sp]
Lloh18:
	adrp	x0, l_.str.5@PAGE
Lloh19:
	add	x0, x0, l_.str.5@PAGEOFF
	bl	_printf
	cbz	x20, LBB6_20
; %bb.12:
Lloh20:
	adrp	x19, l_.str.3@PAGE
Lloh21:
	add	x19, x19, l_.str.3@PAGEOFF
	mov	x21, x20
LBB6_13:                                ; =>This Inner Loop Header: Depth=1
	ldr	w8, [x21]
	str	x8, [sp]
	mov	x0, x19
	bl	_printf
	ldr	x21, [x21, #8]
	cbnz	x21, LBB6_13
; %bb.14:
Lloh22:
	adrp	x0, l_str.9@PAGE
Lloh23:
	add	x0, x0, l_str.9@PAGEOFF
	bl	_puts
	cbz	x20, LBB6_21
; %bb.15:
	ldr	w8, [x20]
	str	x8, [sp]
Lloh24:
	adrp	x0, l_.str.6@PAGE
Lloh25:
	add	x0, x0, l_.str.6@PAGEOFF
	bl	_printf
	ldr	x19, [x20, #8]
	ldr	w21, [x20]
	mov	x0, x20
	bl	_free
	str	x21, [sp]
Lloh26:
	adrp	x0, l_.str.5@PAGE
Lloh27:
	add	x0, x0, l_.str.5@PAGEOFF
	bl	_printf
	cbz	x19, LBB6_19
; %bb.16:
	ldr	w20, [x19]
	mov	x0, x19
	bl	_free
	str	x20, [sp]
Lloh28:
	adrp	x0, l_.str.5@PAGE
Lloh29:
	add	x0, x0, l_.str.5@PAGEOFF
	bl	_printf
	mov	w0, #0
	ldp	x29, x30, [sp, #48]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #32]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #16]             ; 16-byte Folded Reload
	add	sp, sp, #64
	ret
LBB6_17:
Lloh30:
	adrp	x0, l_str@PAGE
Lloh31:
	add	x0, x0, l_str@PAGEOFF
	bl	_puts
	cbnz	x19, LBB6_8
LBB6_18:
Lloh32:
	adrp	x0, l_str.9@PAGE
Lloh33:
	add	x0, x0, l_str.9@PAGEOFF
	bl	_puts
LBB6_19:
Lloh34:
	adrp	x0, l_str.7@PAGE
Lloh35:
	add	x0, x0, l_str.7@PAGEOFF
	b	LBB6_22
LBB6_20:
Lloh36:
	adrp	x0, l_str.9@PAGE
Lloh37:
	add	x0, x0, l_str.9@PAGEOFF
	bl	_puts
LBB6_21:
Lloh38:
	adrp	x0, l_str.8@PAGE
Lloh39:
	add	x0, x0, l_str.8@PAGEOFF
LBB6_22:
	bl	_puts
	mov	w0, #1
	bl	_exit
	.loh AdrpAdd	Lloh10, Lloh11
	.loh AdrpAdd	Lloh12, Lloh13
	.loh AdrpAdd	Lloh14, Lloh15
	.loh AdrpAdd	Lloh16, Lloh17
	.loh AdrpAdd	Lloh18, Lloh19
	.loh AdrpAdd	Lloh20, Lloh21
	.loh AdrpAdd	Lloh22, Lloh23
	.loh AdrpAdd	Lloh26, Lloh27
	.loh AdrpAdd	Lloh24, Lloh25
	.loh AdrpAdd	Lloh28, Lloh29
	.loh AdrpAdd	Lloh30, Lloh31
	.loh AdrpAdd	Lloh32, Lloh33
	.loh AdrpAdd	Lloh34, Lloh35
	.loh AdrpAdd	Lloh36, Lloh37
	.loh AdrpAdd	Lloh38, Lloh39
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str.3:                               ; @.str.3
	.asciz	"%d -> "

l_.str.5:                               ; @.str.5
	.asciz	"Popped: %d\n"

l_.str.6:                               ; @.str.6
	.asciz	"Peek: %d\n"

l_str:                                  ; @str
	.asciz	"Memory allocation error"

l_str.7:                                ; @str.7
	.asciz	"Stack underflow"

l_str.8:                                ; @str.8
	.asciz	"Stack is empty"

l_str.9:                                ; @str.9
	.asciz	"NULL"

.subsections_via_symbols
