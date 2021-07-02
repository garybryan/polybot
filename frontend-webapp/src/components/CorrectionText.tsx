import React, { Fragment } from 'react'
import { Correction } from '../interfaces/interfaces'
import ReactTooltip from 'react-tooltip'

interface CorrectionProps {
  text: string
  correction: Correction
  correctionId: string
  isSelected: boolean
  setSelectedCorrection(correction: Correction): void
}

export default function CorrectionText({
  text,
  correction,
  correctionId,
  isSelected,
  setSelectedCorrection
}: CorrectionProps) {
  const tipId = `correction-tip-${correctionId}`

  return (
    <Fragment>
      <span
        className={`Correction${isSelected ? ' Selected' : ''}`}
        onClick={() => setSelectedCorrection(correction)}
        data-tip
        data-for={tipId}
      >
        {text}
      </span>
      <ReactTooltip id={tipId}>
        <p>{correction.message}</p>
        {correction.suggestions.length && (
          <strong>
            Suggestion{correction.suggestions.length !== 1 ? 's' : ''}
          </strong>
        )}
        <ul>
          {correction.suggestions.map((suggestion, index) => (
            <li key={index}>{suggestion.value}</li>
          ))}
        </ul>
      </ReactTooltip>
    </Fragment>
  )
}
