import React, { Fragment } from 'react'
import { CorrectionLine } from '../interfaces/interfaces'
import CorrectionHighlighter from './CorrectionHighlighter'
import CorrectionItem from './CorrectionItem'

export default function ChatLineCorrection({
  user,
  text,
  corrections
}: CorrectionLine) {
  return (
    <Fragment>
      <strong>{user}: </strong>
      <CorrectionHighlighter text={text} corrections={corrections} />
      {corrections.length ? (
        <Fragment>
          <p>Possible mistakes found:</p>
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
