import React, { Fragment } from 'react'
import { CorrectionLine } from '../interfaces/interfaces'
import CorrectionItem from './CorrectionItem'

export default function ChatLineCorrection({
  user,
  corrections
}: CorrectionLine) {
  return (
    <Fragment>
      <strong>{user}: </strong>
      {corrections.length ? (
        <ul>
          {corrections.map((correction, index) => (
            <CorrectionItem key={index} correction={correction} />
          ))}
        </ul>
      ) : (
        <span>Looks good!</span>
      )}
    </Fragment>
  )
}
