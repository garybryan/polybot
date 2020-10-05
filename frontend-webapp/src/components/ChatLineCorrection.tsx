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
        <Fragment>
          Possible mistakes found
          <ol>
            {corrections.map((correction, index) => (
              <CorrectionItem key={index} correction={correction} />
            ))}
          </ol>
        </Fragment>
      ) : (
        <span>Looks good!</span>
      )}
    </Fragment>
  )
}
