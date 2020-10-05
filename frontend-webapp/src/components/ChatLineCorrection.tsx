import React, { Fragment } from 'react'
import { CorrectionLine } from '../interfaces/interfaces'
import CorrectionItem from './CorrectionItem'

export default function ChatLineCorrection({
  user,
  corrections
}: CorrectionLine) {
  return (
    <Fragment>
      <strong>{user}</strong>: Possible mistakes found:
      {corrections.length ? (
        <ol>
          {corrections.map((correction, index) => (
            <CorrectionItem key={index} correction={correction} />
          ))}
        </ol>
      ) : (
        <span>Looks good!</span>
      )}
    </Fragment>
  )
}
