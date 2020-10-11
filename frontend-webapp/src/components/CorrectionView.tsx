import React from 'react'
import { Correction } from '../interfaces/interfaces'

interface CorrectionViewProps {
  correction: Correction
}

export default function CorrectionView({ correction }: CorrectionViewProps) {
  return (
    <div className="CorrectionView">
      <div className="Message">{correction.message}</div>
      <ul className="Suggestions">
        {correction.suggestions.length > 1 &&
          correction.suggestions.map((suggestion, index) => (
            <li key={index}>
              <em>{suggestion.value}</em>
              {suggestion.short_description &&
                ` (${suggestion.short_description})`}
            </li>
          ))}
      </ul>
    </div>
  )
}
