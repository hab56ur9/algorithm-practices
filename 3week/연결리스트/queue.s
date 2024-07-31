	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 14, 0	sdk_version 14, 4
	.globl	_create_queue                   ; -- Begin function create_queue
	.p2align	2
_create_queue:                          ; @create_queue
	.cfi_startproc
; %bb.0:
	stp	x29, x30, [sp, #-16]!           ; 16-byte Folded Spill
	.cfi_def_cfa_offset 16
	mov	x29, sp
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	mov	w0, #16
	bl	_malloc
	stp	xzr, xzr, [x0]
	ldp	x29, x30, [sp], #16             ; 16-byte Folded Reload
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_enqueue                        ; -- Begin function enqueue
	.p2align	2
_enqueue:                               ; @enqueue
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
	cbz	x0, LBB1_3
; %bb.1:
	str	w20, [x0]
	str	xzr, [x0, #8]
	ldr	x8, [x19, #8]
	cbz	x8, LBB1_4
; %bb.2:
	str	x0, [x8, #8]
	str	x0, [x19, #8]
	b	LBB1_5
LBB1_3:
Lloh0:
	adrp	x0, l_str@PAGE
Lloh1:
	add	x0, x0, l_str@PAGEOFF
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp], #32             ; 16-byte Folded Reload
	b	_puts
LBB1_4:
	stp	x0, x0, [x19]
LBB1_5:
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp], #32             ; 16-byte Folded Reload
	ret
	.loh AdrpAdd	Lloh0, Lloh1
	.cfi_endproc
                                        ; -- End function
	.globl	_dequeue                        ; -- Begin function dequeue
	.p2align	2
_dequeue:                               ; @dequeue
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
	cbz	x0, LBB2_4
; %bb.1:
	ldr	w19, [x0]
	ldr	x9, [x0, #8]
	str	x9, [x8]
	cbnz	x9, LBB2_3
; %bb.2:
	str	xzr, [x8, #8]
LBB2_3:
	bl	_free
	mov	x0, x19
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp], #32             ; 16-byte Folded Reload
	ret
LBB2_4:
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
	ldr	x8, [x0]
	cbz	x8, LBB3_2
; %bb.1:
	ldr	w0, [x8]
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
	ldr	x8, [x0]
	cmp	x8, #0
	cset	w0, eq
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_print_queue                    ; -- Begin function print_queue
	.p2align	2
_print_queue:                           ; @print_queue
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
	ldr	x20, [x0]
	cbz	x20, LBB5_3
; %bb.1:
Lloh6:
	adrp	x19, l_.str.3@PAGE
Lloh7:
	add	x19, x19, l_.str.3@PAGEOFF
LBB5_2:                                 ; =>This Inner Loop Header: Depth=1
	ldr	w8, [x20]
	str	x8, [sp]
	mov	x0, x19
	bl	_printf
	ldr	x20, [x20, #8]
	cbnz	x20, LBB5_2
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
	stp	xzr, xzr, [x0]
	mov	w0, #16
	bl	_malloc
	cbz	x0, LBB6_3
; %bb.1:
	mov	w8, #10
	str	w8, [x0]
	str	xzr, [x0, #8]
	ldr	x8, [x19, #8]
	cbz	x8, LBB6_4
; %bb.2:
	str	x0, [x8, #8]
	str	x0, [x19, #8]
	b	LBB6_5
LBB6_3:
Lloh10:
	adrp	x0, l_str@PAGE
Lloh11:
	add	x0, x0, l_str@PAGEOFF
	bl	_puts
	b	LBB6_5
LBB6_4:
	stp	x0, x0, [x19]
LBB6_5:
	mov	w0, #16
	bl	_malloc
	cbz	x0, LBB6_8
; %bb.6:
	mov	w8, #20
	str	w8, [x0]
	str	xzr, [x0, #8]
	ldr	x8, [x19, #8]
	cbz	x8, LBB6_9
; %bb.7:
	str	x0, [x8, #8]
	str	x0, [x19, #8]
	b	LBB6_10
LBB6_8:
Lloh12:
	adrp	x0, l_str@PAGE
Lloh13:
	add	x0, x0, l_str@PAGEOFF
	bl	_puts
	b	LBB6_10
LBB6_9:
	stp	x0, x0, [x19]
LBB6_10:
	mov	w0, #16
	bl	_malloc
	cbz	x0, LBB6_13
; %bb.11:
	mov	w8, #30
	str	w8, [x0]
	str	xzr, [x0, #8]
	ldr	x8, [x19, #8]
	cbz	x8, LBB6_24
; %bb.12:
	str	x0, [x8, #8]
	str	x0, [x19, #8]
	ldr	x21, [x19]
	cbnz	x21, LBB6_14
	b	LBB6_25
LBB6_13:
Lloh14:
	adrp	x0, l_str@PAGE
Lloh15:
	add	x0, x0, l_str@PAGEOFF
	bl	_puts
	ldr	x21, [x19]
	cbz	x21, LBB6_25
LBB6_14:
Lloh16:
	adrp	x20, l_.str.3@PAGE
Lloh17:
	add	x20, x20, l_.str.3@PAGEOFF
	mov	x22, x21
LBB6_15:                                ; =>This Inner Loop Header: Depth=1
	ldr	w8, [x22]
	str	x8, [sp]
	mov	x0, x20
	bl	_printf
	ldr	x22, [x22, #8]
	cbnz	x22, LBB6_15
; %bb.16:
Lloh18:
	adrp	x0, l_str.9@PAGE
Lloh19:
	add	x0, x0, l_str.9@PAGEOFF
	bl	_puts
	cbz	x21, LBB6_28
; %bb.17:
	ldr	w22, [x21]
	ldr	x20, [x21, #8]
	str	x20, [x19]
	cbz	x20, LBB6_26
; %bb.18:
	mov	x0, x21
	bl	_free
	str	x22, [sp]
Lloh20:
	adrp	x0, l_.str.5@PAGE
Lloh21:
	add	x0, x0, l_.str.5@PAGEOFF
	bl	_printf
Lloh22:
	adrp	x21, l_.str.3@PAGE
Lloh23:
	add	x21, x21, l_.str.3@PAGEOFF
	mov	x22, x20
LBB6_19:                                ; =>This Inner Loop Header: Depth=1
	ldr	w8, [x22]
	str	x8, [sp]
	mov	x0, x21
	bl	_printf
	ldr	x22, [x22, #8]
	cbnz	x22, LBB6_19
; %bb.20:
Lloh24:
	adrp	x0, l_str.9@PAGE
Lloh25:
	add	x0, x0, l_str.9@PAGEOFF
	bl	_puts
	ldr	w8, [x20]
	str	x8, [sp]
Lloh26:
	adrp	x0, l_.str.6@PAGE
Lloh27:
	add	x0, x0, l_.str.6@PAGEOFF
	bl	_printf
	ldr	w22, [x20]
	ldr	x21, [x20, #8]
	str	x21, [x19]
	cbz	x21, LBB6_27
; %bb.21:
	mov	x0, x20
	bl	_free
	str	x22, [sp]
Lloh28:
	adrp	x0, l_.str.5@PAGE
Lloh29:
	add	x0, x0, l_.str.5@PAGEOFF
	bl	_printf
	ldr	w20, [x21]
	ldr	x8, [x21, #8]
	str	x8, [x19]
	cbnz	x8, LBB6_23
; %bb.22:
	str	xzr, [x19, #8]
LBB6_23:
	mov	x0, x21
	bl	_free
	str	x20, [sp]
Lloh30:
	adrp	x0, l_.str.5@PAGE
Lloh31:
	add	x0, x0, l_.str.5@PAGEOFF
	bl	_printf
	mov	w0, #0
	ldp	x29, x30, [sp, #48]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #32]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #16]             ; 16-byte Folded Reload
	add	sp, sp, #64
	ret
LBB6_24:
	stp	x0, x0, [x19]
	ldr	x21, [x19]
	cbnz	x21, LBB6_14
LBB6_25:
Lloh32:
	adrp	x0, l_str.9@PAGE
Lloh33:
	add	x0, x0, l_str.9@PAGEOFF
	bl	_puts
	b	LBB6_28
LBB6_26:
	str	xzr, [x19, #8]
	mov	x0, x21
	bl	_free
	str	x22, [sp]
Lloh34:
	adrp	x0, l_.str.5@PAGE
Lloh35:
	add	x0, x0, l_.str.5@PAGEOFF
	bl	_printf
Lloh36:
	adrp	x0, l_str.9@PAGE
Lloh37:
	add	x0, x0, l_str.9@PAGEOFF
	bl	_puts
Lloh38:
	adrp	x0, l_str.8@PAGE
Lloh39:
	add	x0, x0, l_str.8@PAGEOFF
	b	LBB6_29
LBB6_27:
	str	xzr, [x19, #8]
	mov	x0, x20
	bl	_free
	str	x22, [sp]
Lloh40:
	adrp	x0, l_.str.5@PAGE
Lloh41:
	add	x0, x0, l_.str.5@PAGEOFF
	bl	_printf
LBB6_28:
Lloh42:
	adrp	x0, l_str.7@PAGE
Lloh43:
	add	x0, x0, l_str.7@PAGEOFF
LBB6_29:
	bl	_puts
	mov	w0, #1
	bl	_exit
	.loh AdrpAdd	Lloh10, Lloh11
	.loh AdrpAdd	Lloh12, Lloh13
	.loh AdrpAdd	Lloh14, Lloh15
	.loh AdrpAdd	Lloh16, Lloh17
	.loh AdrpAdd	Lloh18, Lloh19
	.loh AdrpAdd	Lloh22, Lloh23
	.loh AdrpAdd	Lloh20, Lloh21
	.loh AdrpAdd	Lloh26, Lloh27
	.loh AdrpAdd	Lloh24, Lloh25
	.loh AdrpAdd	Lloh28, Lloh29
	.loh AdrpAdd	Lloh30, Lloh31
	.loh AdrpAdd	Lloh32, Lloh33
	.loh AdrpAdd	Lloh38, Lloh39
	.loh AdrpAdd	Lloh36, Lloh37
	.loh AdrpAdd	Lloh34, Lloh35
	.loh AdrpAdd	Lloh40, Lloh41
	.loh AdrpAdd	Lloh42, Lloh43
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str.3:                               ; @.str.3
	.asciz	"%d -> "

l_.str.5:                               ; @.str.5
	.asciz	"Dequeued: %d\n"

l_.str.6:                               ; @.str.6
	.asciz	"Peek: %d\n"

l_str:                                  ; @str
	.asciz	"Memory allocation error"

l_str.7:                                ; @str.7
	.asciz	"Queue underflow"

l_str.8:                                ; @str.8
	.asciz	"Queue is empty"

l_str.9:                                ; @str.9
	.asciz	"NULL"

.subsections_via_symbols
