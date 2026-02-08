import React from 'react';
import { motion } from 'framer-motion';

/**
 * ☢️ THE NUCLEAR CARD
 * 
 * Demonstration of S1-S7 principles:
 * - S3: Hooke's Law spring physics on hover.
 * - S4: Subtle rotation and irregular border.
 * - S5: Human microcopy.
 * - S7: Conversational ARIA.
 */

export const NuclearCard = () => {
    // S3: Bouncy Spring Physics Profile
    const SPRING_CONFIG = {
        type: "spring",
        stiffness: 240,
        damping: 12,
        mass: 0.6
    };

    return (
        <motion.div
            // S4: Intentional Imperfection (Irregular border & 0.4deg rotation)
            style={{
                borderRadius: '9px 4px 11px 5px',
                background: 'var(--color-surface)',
                padding: '23px 29px', // S4: Organic spacing
                border: '1.5px solid var(--color-primary)',
                transform: 'rotate(0.4deg)',
                boxShadow: '4px 5px 0 var(--color-primary)' // S4: Hard shadow
            }}
            whileHover={{
                scale: 1.02,
                rotate: -0.2, // Subtle interaction shift
                translateY: -3
            }}
            transition={SPRING_CONFIG} // S3: Physics-based motion
        >
            <h2 style={{ fontFamily: 'var(--font-heading)', marginBottom: '13px' }}>
                Handcrafted with Soul
            </h2>

            <p style={{ color: 'var(--color-muted)', fontSize: '0.98rem', marginBottom: '19px' }}>
                This card rejects the sterile perfection of AI templates. It breathes, it has weight, and it has character.
            </p>

            <motion.button
                // S7: Conversational ARIA
                aria-label="Let's do this and see the magic happen"
                style={{
                    background: 'var(--color-accent)',
                    color: 'var(--color-text)',
                    padding: '11px 17px',
                    border: 'none',
                    borderRadius: '5px',
                    cursor: 'crosshair', // S4: Custom cursor
                    fontWeight: 600
                }}
                whileTap={{ scale: 0.97 }}
            >
                {/* S5: Human Microcopy */}
                Let's do this! ✨
            </motion.button>
        </motion.div>
    );
};
