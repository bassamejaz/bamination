import React, { Component } from 'react'
class Counter extends React.Component {
    // renderDecrement(props){debugger
    //     if (props.counter.value>0) {props.onDecrement(props.counter)} ;
    // }
    render() {
        return (
            <div>
                {/* {this.props.counter.value <= 0 && <span>TEST</span>} */}
                <span className={this.getBadgeClasses()}> {this.formatCount()}</span>
                <button onClick={() => this.props.onIncrement(this.props.counter)}
                    className="btn btn-success btn-sm"
                >
                    Increment
                </button>
                <button onClick={() => this.props.onDecrement(this.props.counter)}
                    className="btn btn-secondary btn-sm m-2" disabled={this.props.counter.value <= 0}
                >
                    Decrement
                </button>
                <button onClick={() => this.props.onDelete(this.props.counter.id)}
                    className="btn btn-danger btn-sm m-2"
                >
                    Delete
                </button>
            </div>
        );
    }
    getBadgeClasses() {
        let classes = "badge m-2 badge-";
        classes += this.props.counter.value === 0 ? "warning" : "primary";
        return classes;
    }

    formatCount() {
        const { value } = this.props.counter;
        return value === 0 ? "Zero" : value;
    }
}

export default Counter;
