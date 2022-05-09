import { Directive, ElementRef, HostListener, NgModule } from '@angular/core';

@Directive({
  selector: '[appNext]'
})
export class NextDirective {

  constructor(private el:ElementRef) { }

  @HostListener('click')
  nextFunc(){
    var elm = this.el.nativeElement.parentElement.parentElement.children[0];
    var item = elm.getElementsByClassName("item");
    elm.append(item[0]);
  }

}

@NgModule({
  declarations: [ NextDirective ],
  exports: [ NextDirective ]
})

export class NextDirectiveModule {}
